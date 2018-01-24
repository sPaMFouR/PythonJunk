#################################################################
#     To Prefix The Files In A Folder With User Input Date      #
#################################################################

echo -n "Enter Date:"
read var1
for file in ** ; do
mv "${file}" "${var1}_${file}"; done
