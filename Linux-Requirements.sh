checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then

   clear

   printf "\e[1;77mYOUR SHELL : Termux!\n\e[0m"
   echo "----------------------------------------------"
   sleep 3

   pkg install python
   plg install neofetch

   exit 1
fi

}

checkroot

install_linux_pkg() {
 
   clear
   printf "\e[1;77mYOUR SHELL : Linux!\n\e[0m"
   echo "----------------------------------------------"
   sleep 3

   sudo apt install neofetch

   clear
   printf "\e[1;77mYOUR SHELL : Linux!\n\e[0m"
   echo "----------------------------------------------"
   sleep 3

   sudo apt install python3

   clear
   printf "\e[1;77mYOUR SHELL : Linux!\n\e[0m"
}

install_linux_pkg