#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <cstring>
using namespace std;

#define lld long long int

int mod_inverse(int x)
{
  int i,j;
  for(i=1;i<=26;i++)
  {
    j = i*x;
    if(j%26==1)
    {
      return i;
    }
  }
  return i;
}

void getCofactor(int **a, int **temp, int p, int q, int x){
  int i=0,j=0,row,col;

  for(row=0;row<x;row++)
  {
    for(col=0;col<x;col++)
    {

      if(row!=p&&col!=q)
      {
        temp[i][j++] = a[row][col];


      if(j==x-1)
      {
        j=0;
        i++;
      }
    }
  }

}

}

int determinant(int **a, int x,int n){
  int d = 0,i;
  if(x==1)
  {
    return a[0][0];
  }

  int **temp;
  temp = new int* [n];

  for ( i = 0; i < n; ++i) {
  temp[i] = new int[n];

}
  int sign = 1;

  for(i=0;i<x;i++){
    getCofactor(a, temp, 0, i, x);

    d += sign * a[0][i] * determinant(temp, x - 1,n);
    sign = -1*sign;
  }

  return d;
}


void adjoint(int **a,int **adj,int n) {

  if(n==1)
  {
    adj[0][0] = 1;
    return ;
  }

  int sign = 1, **temp,i,j;
  temp = new int* [n];

  for ( i = 0; i < n; ++i) {
  temp[i] = new int[n];

}

  for(i=0;i<n;i++)
  {
    for(j=0;j<n;j++)
    {
      getCofactor(a, temp, i, j, n);
      sign = ((i+j)%2==0)? 1: -1;

      adj[j][i] = (sign)*(determinant(temp, n-1,n));
    }
  }

}



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

      //find inverse of the matrix K.
      n = key_length;
      int **a;
      a = new int* [n];

      for ( i = 0; i < n; ++i) {
      a[i] = new int[n];

    }
      for(i=0;i<n;i++)
      {
        for(j=0;j<n;j++)
        {
           a[i][j] = k[i][j];
        }

      }


      int **adj;
      double inverse[n][n];

      adj = new int* [n];

      for ( i = 0; i < n; ++i) {
      adj[i] = new int[n];

    }

      int det = determinant(a, n, n);

      int d =  mod_inverse(det);

      adjoint(a, adj,n);

      for (i = 0 ;i < n; i++) {

        for (j = 0; j < n; j++) {

           inverse[i][j] = double(d*adj[i][j]);


        }


      }

      ifstream file;
      file.open("cipher_text.txt");
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
            double w=0;
            for(j=i;j<i+key_length;j++)
            {
               w += inverse[c][j-i]*e[j];

               // w = w % 26;
            }
            int w_prime = (int(w))%26;
            if(w_prime<0)
            {
              w_prime = w_prime+ 26;
            }


              f[i+c] = w_prime;


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

      char plaintext[z+x.size()-1];
      c = 0;
      int q=0;

      for(i=0;i<z+x.size()-1;i++)
      {
        if(i==y[c])
        {
          plaintext[i] = ' ';
          c++;
        }
        else{
          plaintext[i] = v[q];
          q++;
        }

       
      }

  return 0;
}
