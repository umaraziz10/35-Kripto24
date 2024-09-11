#include <iostream>
#include <string>

using namespace std;

string shiftCipher (const string& text, int key){
  string hasil = "";

  for (char ch:text){
    if(isalpha(ch)){
      char base = isupper(ch) ? 'A' : 'a';
    
    hasil += static_cast<char>((ch - base + key + 26) % 26 + base);
    }
  }

  return hasil;
}

int main(){
  string input, hasil;
  int key, opt;
  
  cout << "Masukkan kata\n>> ";
  cin >> input;

  cout << "Masukkan Key: (0-25)\n>> ";
  cin >> key;

  cout << "Pilih: 1.Enkripsi 2.Dekripsi\n>> ";
  cin >> opt;

  if(opt == 1){
  string hasil = shiftCipher(input, key);
  cout << "Hasil enkripsi = " << hasil;
  } else if (opt == 2){
    string hasil = shiftCipher(input, -key);
  cout << "Hasil Dekripsi = " << hasil;
  }
  
}