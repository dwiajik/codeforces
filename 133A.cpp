#include <iostream>

using namespace std;

main()
{
	string form;
	cin >> form;
	bool joke =false;
	for(int i=0; i<form.size(); i++)
	{
		if(form[i]=='H' || form[i]=='Q' || form[i]=='9')
		{
			joke = true;
		}
	}
	
	if(joke)
	{
		cout << "YES";
	}
	else
	{
		cout << "NO";
	}
}
