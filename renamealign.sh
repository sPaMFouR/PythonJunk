#########################################
#    To Rename & Copy Aligned Files     #
#########################################

echo -n "Enter Date:"
read var1
for file in *afbs_* ; do
cp "${file}" "${var1}_${file}"; done
cp *_afbs_*.fits /home/avinash/Supernovae_Data/ASASSN14dq/Photometry

