#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <cstring>
using namespace std;
#define lld long long int
int main(int argc, char const *argv[]) {
      int key_length,n,i,j;
      cin >> key_length;
      int k[key_length][key_length];
      string p;
      string r = "";

      vector <string> x;
      vector <int> y;
      for (i=0; i < key_length; i++) {
        for (j = 0; j < key_length; j++) {
          cin >> k[i][j];
        }
      }

      ifstream file;
      file.open("plain_text.txt");
      int h = 0;
      int b = 0;
      while(file >> p){
        x.push_back(p);
        r = r + p;
        h = h + p.length();
        y.push_back(h+x.size()-1);

      }
      int z = r.length();
      int e[z],f[z],c;
      char v[z+5];
      for(i=0;i<z;i++)
      {
          e[i] = r.at(i) - 97;
      }
      int m = z/key_length;
      m = m * key_length;
      for(i=0;i<m;i=i+key_length)
      {
          for(c=0;c<key_length;c++)
          {
            int w=0;
            for(j=i;j<i+key_length;j++)
            {
               w += k[c][j-i]*e[j];
               w = w % 26;
            }
              f[i+c] = w;
          }

      }

      for(i=0;i<z;i++)
      {
        if(i<m){
          v[i] = f[i] + 97;
        }
        else{
          v[i] = e[i] + 97;
        }

      }

      char ciphertext[z+x.size()-1];
      c = 0;
      int q=0;
    
      for(i=0;i<z+x.size()-1;i++)
      {
        if(i==y[c])
        {
          ciphertext[i] = ' ';
          c++;
        }
        else{
          ciphertext[i] = v[q];
          q++;
        }
      }

  return 0;
}
