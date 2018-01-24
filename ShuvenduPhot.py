#!/usr/bin/env python

import os,sys
from astropy.io import ascii
from astropy import table
import pyfits
from pyraf import iraf
from iraf import noao,digiphot,daophot,ptools

from stsci import tools
 
import numpy as np
from glob import glob

import matplotlib.pyplot as plt
from optparse import OptionParser

"""
    INPUT: 
    
        inputImage [string]: the input image you want to use
        aper:  [int]: the aperture for photometry
        sky_annulus [int]: the starting pixel for sky
        width_sky   [int]: the width of the sky annulus in pixels
        plots       [bool]: save plots of the results to disk
    OUTPUT:
        possible plots in PDF form
        the list of object coordinates
        the output photometry results file
        
    FUNCTION:
    
        Run daofind on the input image
	    Run photometry on the given stars, for the CURRENT image, this could be a subtracted image with extra stars in it

	    Dump the resulting star list and phot file

	    REM:     sharp is large positive for blended doubles 
		         close to 0 for stars
			     large negative for crs and blemishes

    
"""
__version__ = "---"
__author__ = "Shuvendu Rakshit"

def strcompress(mystring):
    mystring_compressed = ''.join(mystring.split())
    return mystring_compressed

def message(something):
	"""This is just for displayin simple, short messages that stickout """

	print
 	print "="*len(something)
	print something
	print "="*len(something)
	print


def run(image, fwhm=6.0, sky=8., width=3., plots=False):
    """
    Call this to perform all the following fucntions
    
    Parameters
        image:  string, name of the image
        fwhm:   fwhm of the source to calculate aper size
        sky:    float, where to start the sky aperture
        width:  float, how wide should the sky annulus be
        plots:  bool, save plots of the results for quicklook
        
        
    example:
    
    aperphot.run('myimage.fits',fwhm=6)
    
    """
    
    message("Setting up photometry for %s"%(image))
    coord_list=find_objects(image)
    
    photometry = do_phot(image, coord_list, fwhm=fwhm, sky_annulus=sky, width_sky=width, zeropoint=abzpt)
    
    if plots: plotphot(photometry)
    
    

def find_objects(inputImage):
    """
    Find the objects in the field
    use DAOfind 
    """

    output_locations= inputImage  + ".stars" #best to set this if you're scripting
    
    #check if a file already exists and remove it
    if os.access(output_locations,os.F_OK):
        print "Removing previous star location file"
        os.remove(output_locations)
        
    
    #set up some finding parameters, you can make this more explicit
    iraf.daophot.findpars.threshold=3.0 #3sigma detections only
    iraf.daophot.findpars.nsigma=1.5 #width of convolution kernal in sigma
    iraf.daophot.findpars.ratio=1.0 #ratio of gaussian axes
    iraf.daophot.findpars.theta=0.
    iraf.daophot.findpars.sharplo=0.2 #lower bound on feature
    iraf.daophot.findpars.sharphi=1.0 #upper bound on feature
    iraf.daophot.findpars.roundlo=-1.0 #lower bound on roundness
    iraf.daophot.findpars.roundhi=1.0 #upper bound on roundness
    iraf.daophot.findpars.mkdetections="no"
    
    #assume the science extension
    sci="[SCI,1]"
    message(inputImage + sci)
    iraf.daofind(image=inputImage+sci,output=output_locations,interactive="no",verify="no",verbose="no")

    print "Saved output locations to %s"%(output_locations)
    
    return output_locations #return the name of the saved file

def do_phot(inputImage, coord_list, fwhm, sky_annulus=20, width_sky=20, zeropoint=25.):
    """
    perform aperture photmoetry on the input image at the specified locations
    readnoise and epadu depends on telescope. The values written bellow are for 1.3, 512 * 512CCD
    """
    aper = str(1) + ":" + str(4*float(fwhm)) + ":" + "0.5"
    print "\t Phot aperture: %s pixels"%(aper)
    print "\t Sky Annulus: %i -> %i pixels"%(sky_annulus,sky_annulus+width_sky)


    output = inputImage+ ".phot" #can be anything you like
    if os.access(output,os.F_OK):
        print  "Removing previous photometry file" 
        os.remove(output)
    print "\t Saving output files as %s"%(output)

    iraf.digiphot(_doprint=0)
    iraf.daophot(_doprint=0)

    iraf.datapars.fwhmpsf=4.
    iraf.datapars.datamin=0.0
    iraf.datapars.datamax=200000   #
    iraf.datapars.sigma=4.         #  Standard deviation of background in counts
    iraf.datapars.readnoise=4.3     #  Depending on CCD
    iraf.datapars.epadu=1.4         #  Gain e/ADU; 1 frame
    
    iraf.centerpars.calgorithm='none'
    iraf.centerpars.cbox=5
    iraf.fitskypars.annulus=sky_annulus  #  Inner radius of sky annulus in scale units
    iraf.fitskypars.dannulus=width_sky   #  Width of sky annulus in scale units
    
    iraf.photpars.apertures=aper
    iraf.photpars.zmag=zeropoint
    iraf.photpars.weighting="constant"
    iraf.photpars.mkapert="no"

    iraf.daophot.phot.interactive="no"
    iraf.daophot.phot.verify="no"
    iraf.daophot.phot.verbose="no"
    
    iraf.fitskypars.salgo="mode"
    '''
    iraf.fitskypars.skyval=0
    iraf.fitskypars.smaxi=10
    iraf.fitskypars.sloc=0
    iraf.fitskypars.shic=0
    iraf.fitskypars.snrej=50
    iraf.fitskypars.slorej=3.
    iraf.fitskypars.shirej=3.
    iraf.fitskypars.khist=3
    iraf.fitskypars.binsi=0.1
    '''

    #inputImage =inputImage + "[SCI,1]" #assumed, might be risky
    iraf.daophot.phot.coords=coord_list
    iraf.daophot.phot.output=output
    #iraf.phot.rdnoise=6.1, iraf.phot.gain=1.4  # on paper
    
    iraf.daophot.phot(inputImage, output=output, coords=coord_list,verbose="no",verify="no",interactive="no")
    return output

def photometry(filenames):
    """
        Do photometry of the files
        
    """
    for item in range(len(filenames)):
        print('Photometry on file', filenames[item][0])
        iraf.imstat(filenames[item][0])
        iraf.display(filenames[item][0],1)
        print ('Press , (comma) on your target to get the coord and then q, but DONT press r \n')
        imx=iraf.imexam(Stdout=1)
        # If there is an error like "# ^SyntaxError: unexpected EOF while parsing" then make imx[2] instead imx[3] in all places. It is mainly a file reading problem
        Xref=eval(imx[1].split()[0])    #Using the first star as ref star for cose shift calculation
        Yref=eval(imx[1].split()[1])
        if(imx[1].split()[10]=='INDEF'):
            fwhm=4.0
            print ('fwhm:', 'INDEF', 'but taken as 4.0')
        else:
            fwhm=eval(imx[1].split()[10])
            print ('fwhm:', fwhm)
        print ('Reference cord:', Xref, Yref)
        file1=open('coord_list', 'w')
        file1.write('{0:0.3f}\t{1:0.3f}\n'.format(Xref, Yref))
        file1.close()
        Xref1, Yref1=np.loadtxt('coord_list')
        print('Xref1, Yref1', Xref1, Yref1)
        do_phot(filenames[item][0], 'coord_list', fwhm=fwhm, sky_annulus=10.0, width_sky=10.,zeropoint=25.)
    
    print('All photometry is done. Enjoy! Check .phot file')


def daophot(inp,fwhm):
    iraf.digiphot(_doprint=0)
    iraf.daophot(_doprint=0)
    
    iraf.datapars.fwhmpsf=float(fwhm)
    iraf.datapars.datamin=10
    iraf.datapars.datamax=60000
    iraf.datapars.sigma=50
    iraf.datapars.readnoise=2.3
    iraf.datapars.epadu=0.8
    
    iraf.centerpars.calgorithm='centroid'
    iraf.centerpars.cbox=6
    
    iraf.fitskypars.annulus=20
    iraf.fitskypars.dannulus=10
    
    app = str(fwhm) + ":" + str(4*float(fwhm)) + ":" + "1"
    iraf.photpars.apertures=app
    iraf.photpars.zmag=25
    
    iraf.phot(image=inp, output='default', verify='No', verbose='No',
              coords='default')


def plotphot(photdata,ftype="pdf"):
    """
    neato phot plots from the output files
    use the astropy library to read the input files
    make sure you have astropy0.2 or later installed or it might fail to read correctly
    """
    print photdata
    outfile=photdata + "." + ftype

    #read the ascii table into an astropy.table
    reader=ascii.Daophot()
    photfile = reader.read(photdata)
    

    #remove the points that had issues
    noerror=np.where(photfile[:]['PERROR'] == 'NoError')
    goodphot=photfile[noerror[0][:]]
    indef=np.where(goodphot["MAG"] != "INDEF")
    phot=goodphot[indef[0][:]]
    

    plt.ioff() #turn off interactive so plots dont pop up 
    plt.figure(figsize=(8,10)) #this is in inches
    
    
    mag=phot["MAG"].astype(np.float)
    merr=phot["MERR"].astype(np.float)

    #mag vs merr
    plt.subplot(221)
    plt.xlabel('MAG')
    plt.ylabel('MERR')
    plt.plot(mag,merr,'bx')
    plt.title(photdata,{'fontsize':10})

    #magnitude histogram
    plt.subplot(222)
    plt.xlabel('mag')
    plt.ylabel('Number')
    plt.hist(mag,10)
    plt.xlim(19,29)
    
    #overplot the cummulative curve
    normHist, bins,patches = plt.hist(mag, bins=10, normed=False)
    plt.title('Mag distribution',{'fontsize' : 10})

    xsh=phot["XSHIFT"].astype(np.float)
    ysh=phot["YSHIFT"].astype(np.float)
    #xshift and yshifts, just to see
    plt.subplot(223)
    plt.xlabel('XSHIFT')
    plt.ylabel('YSHIFT')
    plt.plot(xsh,ysh,'bx')
    plt.title('Xshift vs Yshift of centers',{'fontsize':10})
    
    #a quick reference plot of the image and starlocations
    x=phot["XCENTER"].astype(np.float)
    y=phot["YCENTER"].astype(np.float)
    imname=phot["IMAGE"][0].split("[")[0]#assume all from 1 image, and remove extension (careful here)
    image=pyfits.getdata(imname)    
    plt.subplot(224)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(x,y,'ko',mfc="None")
    zero=np.where(image <= 0)
    image[zero]=0.999
    plt.imshow(np.log10(image),cmap=plt.cm.gray)
    plt.title('Total Non-error Stars: %i'%(len(phot)),{'fontsize':10})
    
    plt.tight_layout()
    

    plt.savefig(outfile)
    print "saved output figure to %s"%(outfile)
    

def plotfind(findata,ftype="pdf"):
    """
    plot just the data from the stellar locations file
    """

    outfile=findata+"."+ftype

    #read the ascii table into an astropy.table
    reader=ascii.Daophot()
    photfile = reader.read(findata)
    

    #remove the points that had issues
    noerror=np.where(photfile[:]['PERROR'] == 'NoError')
    goodphot=photfile[good[0][:]]
    indef=np.where(goodphot["MAG"] != "INDEF")
    phot=goodphot[indef[0][:]]



    plt.figure(figsize=(8,10)) #this is in inches
    plt.title('Total Stars Detected %i'%(len(phot)))
    
    mag=phot["MAG"].astype(np.float)
    merr=phot["MERR"].astype(np.float)

    #plots from the finder program
    #sharpness histogram from the detection file
    plt.subplot(222)
    plt.xlabel('Sharpness')
    plt.ylabel('Number')
    hist,bins,p=plt.hist(sharp,10,normed=False)
    plt.title('Detection Types',{'fontsize':10})
    #plt.legend(['Stars','Blends','Blemish'],loc='upper left')
    delta=max(hist)/len(bins)
    yy=max(hist)-delta
    plt.text(bins[0],yy,'Stars at zero',{'color' :'black', 'fontsize' : 10})
    plt.text(bins[0],yy-delta*1.5,'Blends Positive',{'color' :'black', 'fontsize' : 10})
    plt.text(bins[0],yy-delta*2.5,'Blemish Negative',{'color': 'black','fontsize': 10})


    #chi  relation
    plt.subplot(224)
    plt.xlabel('chi')
    plt.ylabel('mag')
    #plt.hist(chi<2,10,normed=False)
    u=np.where(sharp < 1.5)
    uu=np.where(sharp[u] > 0.5)
    schi=chi[uu]
    smag=mag[uu]
    plt.plot(schi,smag,'bx')
    plt.xlim(0,2)
    plt.title('CHI-ball for stars (0.5<sharp>1.5)',{'fontsize': 10})
    plt.savefig(outfile)

    return ofile

def cross_corr(x, y):
    """
        http://stackoverflow.com/q/14297012/190597
        http://en.wikipedia.org/wiki/Autocorrelation#Estimation
        """
    nx, ny = len(x), len(y)
    vx, vy = x.var(), y.var()
    x = x-x.mean()
    y = y-y.mean()
    r = np.correlate(x, y, mode = 'full')
    #assert np.allclose(r, np.array([(x[:n-k]*x[-(n-k):]).sum() for k in range(n)]))
    result = r/(np.sqrt(vx*vy))
    return result


if __name__ == "__main__":  #this tells the os what to do if you called the script from a command shell

    if(not(os.access(options.inputImage,os.F_OK))):
	    print "Unable to access input Image: ",options.inImage
	    sys.exit(0)

    run(inputImage,fwhm=6.0, sky=8., width=3., plots=False)
    print "\nPhotometry is simple and nice\n\n"

