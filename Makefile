#  **************************************************************************  #
#            .      .@@                                                        #
#           $@#.@#$..@$@`     $                                                #
#         `##@$@@@$$$#@$##@@@#                                                 #
#      $@@##@$$###$##@@@@@@#$$@@#                                              #
#     `#$$$##################@`                                                #
#     #$##^$################$#$       Makefile                                 #
#    #$#<--->@#######$##########.                                              #
#    ####$v####.        `####$ #.     By: cdivry <>                            #
#    ####$####$`        .###  .                                                #
#     .########################                                                #
#      .$#$###################.                                                #
#        `#################$.                                                  #
#          `$$############$.`     Created: 2018/10/10 09:54:18 by cdivry       #
#            `#$##########.       Updated: 2018/10/10 09:54:18 by cdivry       #
#               `$#$$$$#$                                                      #
#                   ##$.                                                       #
#  **************************************************************************  #

#SHELL ::= /bin/bash


# DEPENDECIES :
# - virtualenv
# - python3-pip
# - python3-tk


ENV=env
PYT3 := $(shell which python3)
PIP3 := $(shell which pip3)
PYTK := $(shell dpkg -l | grep python3-tk)

R=\033[0;31m
G=\033[0;32m
Y=\033[0;33m
N=\033[0;0m

#######

all: $(ENV) final

clean:
	# rm .pyc but norme forbid wildcards

fclean:
	rm -fr $(ENV)

re: fclean all

#######

.PHONY: all clean fclean re

#######

$(ENV):
	virtualenv -q -p python3 env
	( . env/bin/activate; pip install numpy; pip install -r requirements.txt; )
ifeq ("$(PYTK)", "")
	@echo "$(R) python3-tk not found.$(N)"
	@unknown_command
endif

final:
	@echo ""
	@echo " INSTALLATION TERMINEE AVEC SUCCESS"
	@echo " "
	@echo " pour activier l'environnement :"
	@echo "$(G) source $(ENV)/bin/activate$(N)"

