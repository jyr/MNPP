#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
  switch(argc) {
    case 2:
      mnpp(argv[1], "");
      break;
    case 3:
      mnpp(argv[1], argv[2]);
      break;
    default:
      usage();
      break;
  }
}

int mnpp(char proccess[], char service[]) {
  char command[50];
  
  if (strlen(service) > 0) {
    if (strcmp(proccess,"--start") == 0) {

      sprintf(command, "sh /Applications/MNPP/init/%s.sh start", service);
      printf("command %s", command);
      system(command);
      
    } else if( strcmp(proccess,"--stop") == 0){
      sprintf(command, "sh /Applications/MNPP/init/%s.sh stop", service);
      printf("command %s", command);
      system(command);
    }
    printf("Proccess %s services: %s \n", proccess, service);
  } else {
    if (strcmp(proccess,"--start") == 0) {      

      system("sh /Applications/MNPP/init/start.sh");

    } else if( strcmp(proccess,"--stop") == 0){

      system("sh /Applications/MNPP/init/stop.sh");

    }
  }
  
}

int usage() {
  printf("Usage: \n\t Start");
  printf("\n\t\t sudo mnpp --start");
  printf("\n\t Start only one service");
  printf("\n\t\t sudo mnpp --start [service]");
  printf("\n\t Stop");
  printf("\n\t\t sudo mnpp --stop");
  printf("\n\t Stop only one service");
  printf("\n\t\t sudo mnpp --stop [service]");
  printf("\nService: \n\t nginx | percona | php \n");
}