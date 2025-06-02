#script to clean an amplicon processing folder

confirm() {
    read -p "$1 (y/n)? " response
    case "$response" in
        [Yy]* ) return 0;;  # Return 0 if response starts with y or Y
        [Nn]* ) return 1;;  # Return 1 if response starts with n or N
        * ) echo "Please answer yes or no" && return 1;;
    esac
}


if confirm "Are you sure you want to erase outputs of the amplicon workflow? This can not be undone."; then
	rm -r Figures 
	rm -r Intermediates
	rm -r Logs
	rm -r Output
	rm -r Reads_forSRA
	rm run.log
	rm settings.txt
	rm AmpliconSeq_q2.html
else
	echo "Not erasing"
fi
