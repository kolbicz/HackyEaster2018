#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void decrypt (unsigned int* v, const unsigned int* k) {
    unsigned int v0=v[0], v1=v[1], sum=0xC6EF3720, i;
    unsigned int delta=0x9e3779b9;                   
    unsigned int k0=k[0], k1=k[1], k2=k[2], k3=k[3]; 
    for (i=0; i<32; i++) {                         
        v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
        v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        sum -= delta;                                   
    }                                              
    v[0]=v0; v[1]=v1;
}

int main(int argc, char* argv[]) {  	

	char key[10] = "";
	char pass[20] = "";
	int len = 8;
	const unsigned char png[] = { 0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A };
	char letters[] = "GEARIOTNSLCUDPMHBFYWKVXZJQ[]^_@\\";
	int nbletters = sizeof(letters)-1;
	int i, entry[len];
	int count;
    for(i=0 ; i<len ; i++) entry[i] = 0;
    do {
        for(i=0 ; i<len ; i++) key[i] = letters[entry[i]];
        
        snprintf(pass, 20, "%s%s", key, key);
        char block[] = "\x50\xCB\xB5\xD5\x64\x83\x4F\xFE";
  		decrypt((unsigned int *)block, (unsigned int *)pass);
        
		if(memcmp(block, png, sizeof png) == 0){
			printf("key found : %s\n", key);
			return 0;
		}		
    	
        for(i=0 ; i<len && ++entry[i] == nbletters; i++) entry[i] = 0;        
        if (count % 5000000 == 0) printf("%s\n", pass); // log some info about key progress
        count++;
    } while(i<len);

	return 0;
} 