#include <stdio.h>

int main(int argc, char *argv[]) {

	if( argc <= 2){
		usage();
	}else if( ((strcmp(argv[1], "start") == 0) || (strcmp(argv[1], "restart") == 0) || (strcmp(argv[1], "stop") == 0)) \
									&& ((strcmp(argv[2], "52") == 0) || (strcmp(argv[2], "53") == 0) || (strcmp(argv[2], "54") == 0) )){
		mnpp(argv[1], argv[2]);
	}else if( ((strcmp(argv[1], "nginx") == 0) || (strcmp(argv[1], "percona") == 0))){
		manager(argv[1], argv[2], NULL);
	}else if( (strcmp(argv[1], "php") == 0) && argc == 4 \
									&& ((strcmp(argv[2], "52") == 0) || (strcmp(argv[2], "53") == 0) || (strcmp(argv[2], "54") == 0) )){
		manager(argv[1], argv[2], argv[3]);
	}else{
		usage();
	}

	return 0;
}

int usage(){
  printf("Usage: \n\t All");
  printf("\n\t\t sudo mnpp [Option] [Version]");
  printf("\n\t Only one service");
  printf("\n\t\t sudo mnpp [Service] [Option]");
  printf("\n\t For php");
  printf("\n\t\t sudo mnpp php [Option] [Version]");
  printf("\nVersion: \n\t 52 | 53 | 54 \n");
  printf("\nService: \n\t nginx | percona | php \n");
  printf("\nOption: \n\t start | stop | restart \n");
}

int mnpp(char proccess[], char version[]) {
  char command[50];
  sprintf(command, "sh /Applications/MNPP/init/%s.sh %s", proccess, version);
  system(command);
}

int manager(char service[], char proccess[], char version[]){
  char command[50];
	if(version == NULL){
	  sprintf(command, "sh /Applications/MNPP/init/%s.sh %s", service, proccess);
	}else{
	  sprintf(command, "sh /Applications/MNPP/init/%s.sh %s %s", service, version, proccess);
	}
  system(command);
}
