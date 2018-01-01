#include <iostream>

using namespace std;

main()
{
  int n;
  cin >> n;
  int result = 0;
  string temp;
  for (int i = 0; i < n; i++)
  {
    cin >> temp;
    if(temp[0] == '+' || temp[2] == '+')
    {
      result++;
    }
    if(temp[0] == '-' || temp[2] == '-')
    {
      result--;
    }
  }
  cout << result;
}
