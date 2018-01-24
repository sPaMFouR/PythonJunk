###################################################################
#    To Prefix The Photometric Standards With User Input Date     #
###################################################################

echo -n "Enter Date:"
read var1
for file in *fbs_PG* ; do
mv "${file}" "${var1}_${file}"; done
cp *_fbs_PG* /home/avinash/Supernovae_Data/ASASSN14dq/Standards
