#include <iostream>
using namespace std;

void f(int **a,int x,int y)
{
  a[x][y] = 0;
}
int main(){
  int n,i,j;
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
      cout << a[i][j] << " ";
    }

  }

  f(a,0,1);

  for(i=0;i<n;i++)
  {
    for(j=0;j<n;j++)
    {
      cout <<  a[i][j] << " ";
    }

  }

  cout << endl;
}
