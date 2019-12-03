#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <stdio.h>

void handleErrors(void)
{
    ERR_print_errors_fp(stderr);
    abort();
}


void sha256(unsigned char **digest, unsigned int *digest_len, const unsigned char *message, unsigned int message_len)
/* Use in python: hashmodule.sha256("mymessage")
   
   SWIG specifics:
   **digest, *digest_len are used to return bytes from C to Python - you do not pass them via Python
   message_len allows passing Python strings - you do not pass them via Python
*/
{
	EVP_MD_CTX *mdctx;

	if((mdctx = EVP_MD_CTX_create()) == NULL)
		handleErrors();

	if(1 != EVP_DigestInit_ex(mdctx, EVP_sha256(), NULL))
		handleErrors();

	if(1 != EVP_DigestUpdate(mdctx, message, message_len))
		handleErrors();

	if((*digest = (unsigned char *)OPENSSL_malloc(EVP_MD_size(EVP_sha256()))) == NULL)
		handleErrors();

	if(1 != EVP_DigestFinal_ex(mdctx, *digest, digest_len))
		handleErrors();

	EVP_MD_CTX_destroy(mdctx);
}
