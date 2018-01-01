#include <iostream>

using namespace std;

main()
{
  int n;
  cin >> n;
  char form[n];
  int seq = 0;
  char temp;
  cin >> form;
  for(int i=0; i<n; i++)
  {
    if(form[i] == temp)
    {
      seq++;
    }
    temp=form[i];
  }

  cout << seq;
}
