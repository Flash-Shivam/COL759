#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <cstring>
#include<tuple>
using namespace std;

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


int main() {

  int key_length,i,j;
  int k_prime;
  char trigraph[3][4];
  key_length = 3;
  cin >>  trigraph[0] >> trigraph[1] >> trigraph[2];
  //cout << key_length << " " << digraph1 << " " << digraph2  << endl;
  int k[key_length][key_length];
  int count[26][26][26],f;
  for(i=0;i<26;i++)
  {
    for(j=0;j<26;j++)
    {
      for(f=0;f<26;f++)
      {
        count[i][j][f] = 0;
      }
    }
  }
  ifstream file;
  file.open("ciphertext.txt");
  int h = 0;
  string p;
  string r = "";
  int b = 0;
  vector <string> x;
  vector <int> y;
  while(file >> p){
    x.push_back(p);
    r = r + p;
    h = h + p.length();
    y.push_back(h+x.size()-1);

  }

  k_prime = r.length();



  for(i=0;i<k_prime-2;i++)
  {
    if(r[i]<97)
    {
      r[i] = r[i] + 32;
    }

     count[r[i]-97][r[i+1]-97][r[i+2]-97]++;

  }

  pair <int, tuple <int,int,int > > index[17576];
  int t=0;
  for(i=0;i<26;i++)
  {
    for(j=0;j<26;j++)
    {
      for(f=0;f<26;f++)
      {
        tuple <int,int,int> tmp ;
        tmp = make_tuple(i,j,f);
        index[t].first = count[i][j][f];
        index[t].second = tmp;
        t++;
      }
    }
  }

  sort(index,index+t);

  int mat2[3][3];

  int **mat1;
  mat1 = new int* [3];

  for ( i = 0; i < 3; ++i) {
  mat1[i] = new int[3];

}

  for(i=0;i<3;i++)
  {
    for(j=0;j<3;j++)
    {
      mat1[j][i] = trigraph[i][j] - 'a';

    }
  }

  for(i=0;i<3;i++)
  {
    for(j=0;j<3;j++)
    {
      if(j==0)
      mat2[j][i] = get<0>(index[t-1-i].second);

      if(j==1)
      mat2[j][i] = get<1>(index[t-1-i].second);

      if(j==2)
      mat2[j][i] = get<2>(index[t-1-i].second);
    }
  }

  int det = determinant(mat1,3,3);
  det = mod_inverse(det);
  int **adj;
  int n = 3;
  int inverse[n][n];

  adj = new int* [n];

  for ( i = 0; i < n; ++i) {
  adj[i] = new int[n];

}

adjoint(mat1, adj,n);

for (i = 0 ;i < n; i++) {

  for (j = 0; j < n; j++) {

     inverse[i][j] = (det*adj[i][j])%26;


  }


}

  ofstream myfile;
  myfile.open ("key.txt");



for(i=0;i<3;i++)
{
  for(j=0;j<3;j++)
  { int res = 0;
    for(f=0;f<3;f++)
    {
      res = res + mat2[i][f]*inverse[f][j]
    }
    k[i][j] = res;
    myfile << k[i][j] << " ";
  }
  myfile << "\n";
}

myfile.close();

  return 0;
}
