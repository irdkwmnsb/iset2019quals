#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;


struct CharacterInfo {
    double probability;
    double left;
    double right;
};


struct DataInfo {
    char* data;
    CharacterInfo* alphabet;
    int n;

    ~DataInfo() {
        delete[] data;
        delete[] alphabet;
    }
};


char* decode(double encodedData, DataInfo* dataInfo) {
    char* result = new char[32];
    memset(result, 0, 32);
    int currentPtr = 0;

    for (int i = 0; i < dataInfo->n; ++i) {
        for (int j = 0; j < 256; ++j) {
            if (encodedData >= dataInfo->alphabet[j].left && encodedData < dataInfo->alphabet[j].right) {
                result[currentPtr++] = (char)j;
                encodedData = (encodedData - dataInfo->alphabet[j].left) / (dataInfo->alphabet[j].right - dataInfo->alphabet[j].left);
                break;
            }
        }
    }
    return result;
}


int main() {
    FILE *fp;
    fp = fopen("out.pack", "rb");
    char* charactersData = new char[sizeof(CharacterInfo) * 256];
    char* xlam = new char[16];
    int n;
    double result;

    fread(xlam, sizeof(char), 5, fp);
    fread(&result, sizeof(double), 1, fp);
    fread(&n, sizeof(int), 1, fp);
    fread(charactersData, sizeof(CharacterInfo), 256, fp);
    fclose(fp);

    printf( "== Welcome to MAXIKUnPacker2000 ==\n");
    DataInfo* dataInfo = new DataInfo();
    dataInfo->n = n;
    dataInfo->alphabet = (CharacterInfo*)charactersData;
    char* out = decode(result, dataInfo);

    printf("%f\n", result);
    printf("%s\n", out);
    printf("Maxik unpacked your data successfully!\n");
    delete dataInfo;
    delete[] out;
    return 0;
}
