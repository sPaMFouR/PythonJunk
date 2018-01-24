real count = 0.
string frame[500] 
string image
list = "list_files"
while(fscan(list,image)!=EOF)
	{
		count = count+1
	
		imexam (image,1, "", output="", ncoutput=101, nloutput=101,
                logfile="fwhm.coo", keeplog=yes, defkey="a", autoredraw=yes,
                allframes=yes, nframes=0, ncstat=25, nlstat=25,graphcur="", imagecur="stars.coo",
                wcs="logical", xformat="", yformat="", graphics="stdgraph",
                display="display(image='$1',frame=$2)", use_display=no)

	}

