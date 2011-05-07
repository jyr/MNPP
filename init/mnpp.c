#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {

  if(argc == 1 || argc == 2 || argc > 3) {
    usage();
  }else if ( (strcmp(argv[1], "--php52") == 0) || (strcmp(argv[1], "--php53") == 0) ){
    if((strcmp(argv[2], "--start") == 0) || (strcmp(argv[2], "--stop") == 0)){
      mnpp(argv[1], argv[2], "");
    }else{
      usage();
    }
  } else if( (strcmp(argv[1], "--start") == 0) || (strcmp(argv[1], "--stop") == 0) ){
    if((strcmp(argv[2], "php52") == 0) || (strcmp(argv[2], "php53") == 0) || (strcmp(argv[2], "percona") == 0) || (strcmp(argv[2], "nginx") == 0)){
      mnpp("", argv[1], argv[2]);
    }else{
      usage();
    }
   
  }
  
}

int mnpp(char phpVersion[], char proccess[], char service[]) {
  char command[50];
  int version;

  if ( (strcmp(phpVersion, "--php52") == 0) || (strcmp(service, "php52") == 0)) {
    version = 52;
  }else if((strcmp(phpVersion, "--php53") == 0) || (strcmp(service, "php53") == 0)) {
    version = 53;
  }

  if ((strcmp(phpVersion, "") == 0)) {
    if (strcmp(proccess,"--start") == 0) {

      if((strcmp(service, "php52") == 0) || (strcmp(service, "php53") == 0)) {
        sprintf(command, "sh /Applications/MNPP/init/php.sh %i start", version);
      }else {
        sprintf(command, "sh /Applications/MNPP/init/%s.sh start", service);
      }
      system(command);
      
    } else if( strcmp(proccess,"--stop") == 0){

      if((strcmp(service, "php52") == 0) || (strcmp(service, "php53") == 0)) {
        sprintf(command, "sh /Applications/MNPP/init/php.sh %i stop", version);
      }else{
        sprintf(command, "sh /Applications/MNPP/init/%s.sh stop", service);
      }
      system(command);
    }
  } else {
    if (strcmp(proccess,"--start") == 0) {      
      sprintf(command, "sh /Applications/MNPP/init/start.sh %i", version);
      system(command);

    } else if( strcmp(proccess,"--stop") == 0){
      sprintf(command, "sh /Applications/MNPP/init/stop.sh %i", version);
      system(command);

    }
  }
  //printf("command %s", command);
  
  return(0);
}

int usage() {
  printf("Usage: \n\t Start");
  printf("\n\t\t sudo mnpp --php[Version] --start");
  printf("\n\t Start only one service");
  printf("\n\t\t sudo mnpp --start [service]");
  printf("\n\t For php");
  printf("\n\t\t sudo mnpp --start php[Version]");
  printf("\n\t Stop");
  printf("\n\t\t sudo mnpp --php[Version] --stop");
  printf("\n\t Stop only one service");
  printf("\n\t\t sudo mnpp --stop [service]");
  printf("\n\t For php");
  printf("\n\t\t sudo mnpp --stop php[Version]");
  printf("\nVersion: \n\t 52 | 53 \n");
  printf("\nService: \n\t nginx | percona | php \n");
}