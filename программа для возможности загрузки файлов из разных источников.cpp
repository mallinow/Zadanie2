#include <iostream>
#include <fstream>
#include <curl/curl.h>

using namespace std;

// функция для загрузки файла из Интернета
size_t download_file(const char* url, const char* filename) {
    CURL* curl = curl_easy_init();
    if (!curl) {
        return -1;
    }

    FILE* fp = fopen(filename, "wb");
    if (!fp) {
        return -1;
    }

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, fwrite);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);

    CURLcode res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    fclose(fp);

    return res;
}

int main() {
    // загрузка файла из Интернета
    const char* url = "https://example.com/remote_file.txt";
    const char* filename = "remote_file.txt";
    if (download_file(url, filename) == CURLE_OK) {
        cout << "Файл успешно загружен" << endl;
    } else {
        cout << "Ошибка загрузки файла" << endl;
    }

    // загрузка файла с локального диска
    ifstream fin("local_file.txt", ios::binary);
    if (fin) {
        ofstream fout("uploaded_file.txt", ios::binary);
        fout << fin.rdbuf();
        fout.close();
        cout << "Файл успешно загружен" << endl;
    } else {
        cout << "Ошибка загрузки файла" << endl;
    }

    return 0;
}
