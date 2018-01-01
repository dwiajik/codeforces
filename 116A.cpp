#include <iostream>

using namespace std;

main()
{
  int n;
  cin >> n;
  int pass = 0, passMin = 0;
  int temp;
  for (int i = 0; i < n; i++)
  {
    cin >> temp;
    pass -= temp;
    cin >> temp;
    pass += temp;
    if(pass > passMin)
    {
      passMin = pass;
    }
  }
  cout << passMin;
}
