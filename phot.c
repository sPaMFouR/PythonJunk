#include <stdio.h>
#include <math.h>

float us, bs, vs, rs, is, usum, bsum, vsum, rsum, isum, apc_u, apc_b, apc_v, apc_r, apc_i, avbeta_u, avbeta_b, avbeta_v, avbeta_r, avbeta_i;
float sdu1, sdu2, sdu3, sdb1, sdb2, sdb3, sdv1, sdv2, sdv3, sdr1, sdr2, sdr3, sdi1, sdi2, sdi3, snu_err, snb_err, snv_err, snr_err, sni_err;
float apu_mag1[20], apu_mag2[20], apb_mag1[20], apb_mag2[20], apv_mag1[20], apv_mag2[20], apr_mag1[20], apr_mag2[20], api_mag1[20], api_mag2[20];
float apu12[20], apb12[20], apv12[20], apr12[20], api12[20], au[20], ab[20], av[20], ar[20], ai[20], beta_u[20], beta_b[20], beta_v[20], 
beta_r[20], beta_i[20];
float u_psf[20], b_psf[20], v_psf[20], r_psf[20], i_psf[20], u_err[20], b_err[20], v_err[20], r_err[20], i_err[20], psfc_u[20], psfc_b[20], psfc_v[20], psfc_r[20], psfc_i[20];
float psfcor_u, psfcor_b, psfcor_v, psfcor_r, psfcor_i, snu, snb, snv, snr, sni, snerr_u, snerr_b, snerr_v, snerr_r, snerr_i, snu_mag, snb_mag, snv_mag, snr_mag, sni_mag;
 
 main()
{

int i,j,id=0;
FILE *fp1, *fp2, *fp3, *fp4, *fp5, *fp6, *fp7, *fp8, *fp9, *fp10, *fp11, *fp12, *fp13, *fp14, *fp15, *fp16;

fp1 = fopen("apr_magu", "r");
fp2 = fopen("apr_magb", "r");
fp3 = fopen("apr_magv", "r");
fp4 = fopen("apr_magr", "r");
fp5 = fopen("apr_magi", "r");

/* aperture correction*/

for(i=0;i<=14;i++)
{
fscanf(fp1, "%d %f %f \n", &id, &apu_mag1[i], &apu_mag2[i]);
fscanf(fp2, "%d %f %f\n", &id, &apb_mag1[i], &apb_mag2[i]);
fscanf(fp3, "%d %f %f\n", &id, &apv_mag1[i], &apv_mag2[i]);
fscanf(fp4, "%d %f %f\n", &id, &apr_mag1[i], &apr_mag2[i]);
fscanf(fp5, "%d %f %f\n", &id, &api_mag1[i], &api_mag2[i]);

apu12[i] = apu_mag1[i] - apu_mag2[i];
apb12[i] = apb_mag1[i] - apb_mag2[i];
apv12[i] = apv_mag1[i] - apv_mag2[i];
apr12[i] = apr_mag1[i] - apr_mag2[i];
api12[i] = api_mag1[i] - api_mag2[i];

printf("%f %f %f %f %f\n", apu12[i], apb12[i], apv12[i], apr12[i], api12[i]);}

fclose(fp1);
fclose(fp2);
fclose(fp3);
fclose(fp4);
fclose(fp5);

apc_u = (apu12[0]+apu12[1]+apu12[2]+apu12[3])/4.0;
apc_b = (apb12[0]+apb12[1]+apb12[2]+apb12[3])/4.0;
apc_v = (apv12[0]+apv12[1]+apv12[2]+apv12[3])/4.0;
apc_r = (apr12[0]+apr12[1]+apr12[2]+apr12[3])/4.0;
apc_i = (api12[1]+api12[2]+api12[3])/3.0;

sdu1 = sqrt((pow((apu12[0]-apc_u),2)+pow((apu12[1]-apc_u),2)+pow((apu12[2]-apc_u),2)+pow((apu12[3]-apc_u),2))/4.0);
sdb1 = sqrt((pow((apb12[0]-apc_b),2)+pow((apb12[1]-apc_b),2)+pow((apb12[2]-apc_b),2)+pow((apb12[3]-apc_b),2))/4.0);
sdv1 = sqrt((pow((apv12[0]-apc_v),2)+pow((apv12[1]-apc_v),2)+pow((apv12[2]-apc_v),2)+pow((apv12[3]-apc_v),2))/4.0);
sdr1 = sqrt((pow((apr12[0]-apc_r),2)+pow((apr12[1]-apc_r),2)+pow((apr12[2]-apc_r),2)+pow((apr12[3]-apc_r),2))/4.0);
sdi1 = sqrt((pow((api12[1]-apc_i),2)+pow((api12[2]-apc_i),2)+pow((api12[3]-apc_i),2))/2.0);

printf("sd1 : %f %f %f %f %f\n", sdu1, sdb1, sdv1, sdr1, sdi1);
printf("Aperture correction : %f %f %f %f %f \n", apc_u, apc_b, apc_v, apc_r, apc_i);

/* zero point correction */

fp6 = fopen("/home/user/sn_data/j1505/field_j1505new","r");

for(i=0;i<=14;i++)
{
fscanf(fp6, "%d %f %f %f %f %f\n", &id, &au[i], &ab[i], &av[i], &ar[i], &ai[i]);

beta_u[i] = au[i] - apu_mag1[i] + apc_u - 0.1895*(au[i]-ab[i]);
beta_b[i] = ab[i] - apb_mag1[i] + apc_b + 0.0530*(ab[i]-av[i]);
beta_v[i] = av[i] - apv_mag1[i] + apc_v - 0.0442*(ab[i]-av[i]);
beta_r[i] = ar[i] - apr_mag1[i] + apc_r - 0.0650*(av[i]-ar[i]);
beta_i[i] = ai[i] - api_mag1[i] + apc_i - 0.0188*(av[i]-ai[i]);

us = us + beta_u[i];
bs = bs + beta_b[i];
vs = vs + beta_v[i];
rs = rs + beta_r[i];
is = is + beta_i[i];
printf("%f %f %f %f %f \n", beta_u[i], beta_b[i], beta_v[i], beta_r[i], beta_i[i]);
}

fclose(fp6);

avbeta_u = us/4.0;
avbeta_b = bs/4.0;
avbeta_v = vs/4.0;
avbeta_r = rs/4.0;
avbeta_i = is/4.0;

printf("\nAverage beta : %f %f %f %f %f \n", avbeta_u, avbeta_b, avbeta_v, avbeta_r, avbeta_i);

us=bs=vs=rs=is=0.0;

for(i=0;i<=14;i++)
{
 us = us + (beta_u[i]-avbeta_u)*(beta_u[i]-avbeta_u);
 bs = bs + (beta_b[i]-avbeta_b)*(beta_b[i]-avbeta_b);
 vs = vs + (beta_v[i]-avbeta_v)*(beta_v[i]-avbeta_v);
 rs = rs + (beta_r[i]-avbeta_r)*(beta_r[i]-avbeta_r);
 is = is + (beta_i[i]-avbeta_i)*(beta_i[i]-avbeta_i);
}

sdu2 = sqrt(us/4.0);
sdb2 = sqrt(bs/4.0);
sdv2 = sqrt(vs/4.0);
sdr2 = sqrt(rs/4.0);
sdi2 = sqrt(is/4.0);

printf("sd2 : %f %f %f %f %f \n", sdu2, sdb2, sdv2, sdr2, sdi2);

/* psf correction */

fp7 = fopen("psf_magu", "r");
fp8 = fopen("psf_magb", "r");
fp9 = fopen("psf_magv", "r");
fp10 = fopen("psf_magr", "r");
fp11 = fopen("psf_magi", "r");

for(i=0;i<=14;i++)
{

fscanf(fp7, "%d %f %f\n", &id, &u_psf[i], &u_err[i]);
fscanf(fp8, "%d %f %f\n", &id, &b_psf[i], &b_err[i]);
fscanf(fp9, "%d %f %f\n", &id, &v_psf[i], &v_err[i]);
fscanf(fp10, "%d %f %f\n", &id, &r_psf[i], &r_err[i]);
fscanf(fp11, "%d %f %f\n", &id, &i_psf[i], &i_err[i]);

psfc_u[i] = apu_mag1[i] - apc_u - u_psf[i];
psfc_b[i] = apb_mag1[i] - apc_b - b_psf[i];
psfc_v[i] = apv_mag1[i] - apc_v - v_psf[i];
psfc_r[i] = apr_mag1[i] - apc_r - r_psf[i];
psfc_i[i] = api_mag1[i] - apc_i - i_psf[i];

//usum = usum + psfc_u[i];
//bsum = bsum + psfc_b[i];
//vsum = vsum + psfc_v[i];
//rsum = rsum + psfc_r[i];
//isum = isum + psfc_i[i];

printf("%f %f %f %f %f \n", psfc_u[i], psfc_b[i], psfc_v[i], psfc_r[i], psfc_i[i]);
}

fclose(fp7);
fclose(fp8);
fclose(fp9);
fclose(fp10);
fclose(fp11);

psfcor_u = (psfc_u[0]+psfc_u[1]+psfc_u[2]+psfc_u[3])/4.0;
psfcor_b = (psfc_b[0]+psfc_b[1]+psfc_b[2]+psfc_b[3])/4.0;
psfcor_v = (psfc_v[0]+psfc_v[1]+psfc_v[2]+psfc_v[3])/4.0;
psfcor_r = (psfc_r[0]+psfc_r[1]+psfc_r[2]+psfc_r[3])/4.0;
psfcor_i = (psfc_i[0]+psfc_i[1]+psfc_i[2]+psfc_i[3])/4.0;

printf("\nPSF corrections : %f %f %f %f %f \n", psfcor_u, psfcor_b, psfcor_v, psfcor_r, psfcor_i);

sdu3 = sqrt((pow((psfc_u[0]-psfcor_u),2)+pow((psfc_u[1]-psfcor_u),2)+pow((psfc_u[2]-psfcor_u),2)+pow((psfc_u[3]-psfcor_u),2))/4.0);
sdb3 = sqrt((pow((psfc_b[0]-psfcor_b),2)+pow((psfc_b[1]-psfcor_b),2)+pow((psfc_b[2]-psfcor_b),2)+pow((psfc_b[3]-psfcor_b),2))/4.0);
sdv3 = sqrt((pow((psfc_v[0]-psfcor_v),2)+pow((psfc_v[1]-psfcor_v),2)+pow((psfc_v[2]-psfcor_v),2)+pow((psfc_v[3]-psfcor_v),2))/4.0);
sdr3 = sqrt((pow((psfc_r[0]-psfcor_r),2)+pow((psfc_r[1]-psfcor_r),2)+pow((psfc_r[2]-psfcor_r),2)+pow((psfc_r[3]-psfcor_r),2))/4.0);
sdi3 = sqrt((pow((psfc_i[0]-psfcor_i),2)+pow((psfc_i[1]-psfcor_i),2)+pow((psfc_i[2]-psfcor_i),2)+pow((psfc_i[3]-psfcor_i),2))/4.0);

printf("\n sd3 : %f %f %f %f %f \n", sdu3, sdb3, sdv3, sdr3, sdi3);

/* reading supernova magnitude */

fp12 = fopen("psf_magu", "r");
fp13 = fopen("psf_magb", "r");
fp14 = fopen("psf_magv", "r");
fp15 = fopen("psf_magr", "r");
fp16 = fopen("psf_magi", "r");

for(j=0;j<=15;j++)
{

fscanf(fp12, "%d %f %f\n", &id, &snu, &snerr_u);
fscanf(fp13, "%d %f %f\n", &id, &snb, &snerr_b);
fscanf(fp14, "%d %f %f\n", &id, &snv, &snerr_v);
fscanf(fp15, "%d %f %f\n", &id, &snr, &snerr_r);
fscanf(fp16, "%d %f %f\n", &id, &sni, &snerr_i);

}

printf("\n SN psf magnitudes : %f %f %f %f %f \n", snu, snb, snv, snr, sni);

fclose(fp12);
fclose(fp13);
fclose(fp14);
fclose(fp15);
fclose(fp16);

snu_mag = snu + avbeta_u + psfcor_u;
snb_mag = snb + avbeta_b + psfcor_b;
snv_mag = snv + avbeta_v + psfcor_v;
snr_mag = snr + avbeta_r + psfcor_r;
sni_mag = sni + avbeta_i + psfcor_i;

snu_err = sqrt(snerr_u*snerr_u + sdu1*sdu1 + sdu2*sdu2 + sdu3*sdu3);
snb_err = sqrt(snerr_b*snerr_b + sdb1*sdb1 + sdb2*sdb2 + sdb3*sdb3);
snv_err = sqrt(snerr_v*snerr_v + sdv1*sdv1 + sdv2*sdv2 + sdv3*sdv3);
snr_err = sqrt(snerr_r*snerr_r + sdr1*sdr1 + sdr2*sdr2 + sdr3*sdr3);
sni_err = sqrt(snerr_i*snerr_i + sdi1*sdi1 + sdi2*sdi2 + sdi3*sdi3);

printf("SN magnitudes (ubvri) : \n");
printf("%0.3f \t %0.3f \t %0.3f \t %0.3f \t %0.3f \n", snu_mag, snb_mag, snv_mag, snr_mag, sni_mag);

printf("Errors in SN magnitudes : \n");
printf("%0.3f \t %0.3f \t %0.3f \t %0.3f \t %0.3f \n", snu_err, snb_err, snv_err, snr_err, sni_err);

return 0;
}
