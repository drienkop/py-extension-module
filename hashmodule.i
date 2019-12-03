/* hashmodule.i */
%module hashmodule

%include <cstring.i>
%cstring_output_allocate_size(char **digest, int *digest_len, free(*$1));

%include <typemaps.i>
%apply char* {unsigned char*};
%apply (char *STRING, int LENGTH) { (char *message, int message_len) };

%{
/* Header files or function declarations go here */
extern void sha256(char **digest, int *digest_len, char *message, int message_len);
%}

extern void sha256(char **digest, int *digest_len, char *message, int message_len);
