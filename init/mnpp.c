#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
  switch(argc) {
    case 3:
      mnpp(argv[1], argv[2], "");
      break;
    case 4:
      mnpp(argv[1], argv[2], argv[3]);
      break;
    default:
      usage();
      break;
  }
}

int mnpp(char phpVersion[], char proccess[], char service[]) {
  char command[50];
  int version;

  if ( strcmp(phpVersion, "--php52") == 0) {
    version = 52;
  }else if(strcmp(phpVersion, "--php53") == 0) {
    version = 53;
  }
  
  if (strlen(service) > 0) {
    if (strcmp(proccess,"--start") == 0) {

      sprintf(command, "sh /Applications/MNPP/init/%s.sh start", service);
      //printf("command %s", command);
      system(command);
      
    } else if( strcmp(proccess,"--stop") == 0){
      sprintf(command, "sh /Applications/MNPP/init/%s.sh stop", service);
      //printf("command %s", command);
      system(command);
    }
    //printf("Proccess %s services: %s \n", proccess, service);
  } else {
    if (strcmp(proccess,"--start") == 0) {      
      sprintf(command, "sh /Applications/MNPP/init/start.sh %i", version);
      system(command);

    } else if( strcmp(proccess,"--stop") == 0){
      sprintf(command, "sh /Applications/MNPP/init/stop.sh %i", version);
      system(command);

    }
  }
  
  return(0);
}

int usage() {
  printf("Usage: \n\t Start");
  printf("\n\t\t sudo mnpp --php[Version] --start");
  printf("\n\t Start only one service");
  printf("\n\t\t sudo mnpp --start [service]");
  printf("\n\t Stop");
  printf("\n\t\t sudo mnpp --php[Version] --stop");
  printf("\n\t Stop only one service");
  printf("\n\t\t sudo mnpp --stop [service]");
  printf("\nVersion: \n\t 52 | 53 \n");
  printf("\nService: \n\t nginx | percona | php \n");
}