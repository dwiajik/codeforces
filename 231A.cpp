#include <iostream>

using namespace std;

main()
{
	int n;
	cin >> n;
	int a=0, b=0, c=0;
	int implement=0;
	for (int i = 0; i < n; i++)
	{
		cin >> a;
		cin >> b;
		cin >> c;
		if(a+b+c >=2)
		{
			implement++;
		}
	}
	cout << implement;
}
