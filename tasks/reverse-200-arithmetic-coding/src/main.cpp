#include <iostream>
#include <cstring>
#include <cstdio>

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

DataInfo* collectDataInfo(char *input) {
    DataInfo *dataInfo = new DataInfo();
    dataInfo->alphabet = new CharacterInfo[256];
    dataInfo->n = strlen(input);
    dataInfo->data = new char[dataInfo->n + 1];
    
    memcpy(dataInfo->data, input, dataInfo->n + 1);
    memset(dataInfo->alphabet, 0, 256 * sizeof(CharacterInfo));
    int *frequencies = new int[256];
    for (int i = 0; i < dataInfo->n; ++i) {
        frequencies[dataInfo->data[i]] ++;
    }
    for (int i = 0; i < 256; ++i) {
        dataInfo->alphabet[i].probability = (double)frequencies[i] / dataInfo->n;
    }

    double pointer = 0;
    for (int i = 0; i < 256; ++i) {
        dataInfo->alphabet[i].left = pointer;
        dataInfo->alphabet[i].right = pointer + dataInfo->alphabet[i].probability;

        pointer = dataInfo->alphabet[i].right;
    }

    return dataInfo;
}


double encode(char* input, DataInfo* dataInfo) {
    double left = 0, right = 1;
    for (int i = 0; i < dataInfo->n; ++i) {
        char currentChar = dataInfo->data[i];

        double newRight = left + (right - left) * dataInfo->alphabet[currentChar].right;
        double newLeft = left + (right - left) * dataInfo->alphabet[currentChar].left;
        left = newLeft;
        right = newRight;
    }

    return (left + right) / 2;
}


int main() {
    FILE *fp;
    DataInfo* dataInfo;
    double result;
    char input[16];

    fp = fopen("out.pack", "wb");

    printf( "== Welcome to MAXIKPacker2000 ==\n");
    printf("Enter your data: ");
    
    scanf("%15s", &input);
    dataInfo = collectDataInfo(input);
    result = encode(input, dataInfo);

    printf("%f\n", result);
    fwrite("MAXIK", sizeof(char), 5, fp);
    fwrite(&result, 1, sizeof(double), fp);
    fwrite(&dataInfo->n, sizeof(int), 1, fp);
    fwrite(dataInfo->alphabet, sizeof(CharacterInfo), 256, fp);
    fclose(fp);
    delete dataInfo;

    printf("MAXIK packed your data successfully!\n");

    return 0;
}
