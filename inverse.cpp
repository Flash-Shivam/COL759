#include <iostream>
#include <algorithm>
using namespace std;



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
  int i,j,k,n;

  cin >> n;
  int **a;
  a = new int* [n];

  for ( i = 0; i < n; ++i) {
  a[i] = new int[n];

}
  for(i=0;i<n;i++)
  {
    for(j=0;j<n;j++)
    {
      cin >> a[i][j];
    }

  }


  int **adj,inverse[n][n];

  adj = new int* [n];

  for ( i = 0; i < n; ++i) {
  adj[i] = new int[n];

}

  int det = determinant(a, n, n);

  adjoint(a, adj,n);

  for (i = 0 ;i < n; i++) {

    for (j = 0; j < n; j++) {

       inverse[i][j] = adj[i][j]/det;

    }

  }
  return 0;
}
