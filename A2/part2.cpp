#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <cstring>
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

int main() {

  int key_length,i,j;
  int k_prime;
  char digraph1[3],digraph2[3];
  cin >> key_length >> digraph1 >> digraph2;
  //cout << key_length << " " << digraph1 << " " << digraph2  << endl;
  int k[key_length][key_length];
  int count[26][26];
  for(i=0;i<26;i++)
  {
    for(j=0;j<26;j++)
    {
      count[i][j] = 0;
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

  // cout << k_prime <<endl;

  for(i=0;i<k_prime-1;i++)
  {
    if(r[i]<97)
    {
      r[i] = r[i] + 32;
    }
    //cout << r[i] << " " << r[i+1] << endl;
     count[r[i]-97][r[i+1]-97]++;
    //cout << r[i]-'97' << "," << r[i+1]-'97' << endl;
  }

  pair <int, pair <int,int > > index[676];
  int t=0;
  for(i=0;i<26;i++)
  {
    for(j=0;j<26;j++)
    {
      pair <int,int> tmp;
      tmp.first = i;
      tmp.second = j;
      index[t].first = count[i][j];
      index[t].second = tmp;
      t++;
    }
  }
//  cout << t << endl;
  sort(index,index+t);
  //cout << "Sorted " << endl;
  //Scout << index[t-1].first << endl;
  int a1 = index[t-1].second.first;
  int a2 =  index[t-1].second.second;
  int b1 = index[t-2].second.first;
  int b2 =  index[t-2].second.second;

  //cout << a1 << " " << b1 << " " <<a2 <<  " " << b2 << endl;

  int c1 = digraph1[0]- 'a';
  int c2 = digraph1[1]- 'a';
  int d1 = digraph2[0]- 'a';
  int d2 = digraph2[1]- 'a';
  //cout << c1 << " " << d1 << " " <<c2 <<  " " << d2 << endl;

  int det = c1*d2 - c2*d1;
//  cout << det << endl;
  det = det  % 26;
  if(det<0)
  {
    det = det + 26;
  }
  det = det  % 26;

  det = mod_inverse(det);
  //cout << det << endl;

  int tmp_var = c1;
  c1 = d2;
  d2 = tmp_var;
  tmp_var = c2;
  c2 = d1;
  d1 = tmp_var;

  tmp_var = c2;
  c2 = d1;
  d1 = tmp_var;
  c2 = -c2;
  d1 = -d1;
  c1 = (26+(det*c1)%26)%26;
  c2 = (26+(det*c2)%26)%26;
  d1 = (26+(det*d1)%26)%26;
  d2 = (26+(det*d2)%26)%26;

  //cout << c1 << " " << d1 << " " <<c2 <<  " " << d2 << endl;

  k[0][0] = (a1*c1 + b1*c2 )%26;
  k[0][1] = (a1*d1 + b1*d2 )%26;
  k[1][1] = (a2*d1+b2*d2)%26;
  k[1][0] = (a2*c1+b2*c2)%26;
  ofstream myfile;
  myfile.open ("key.txt");
  for(i=0;i<2;i++)
  {
    for(j=0;j<2;j++)
    {
      myfile << k[i][j] << " ";
     }
     myfile << "\n";
  }
  myfile.close();
  return 0;
}
