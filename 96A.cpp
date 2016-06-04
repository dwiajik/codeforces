#include <iostream>

using namespace std;

main()
{
	string form;
	int maxSeq = 0, seq = 1;
	char temp;
	cin >> form;
	for(int i=0; i<form.size(); i++)
	{
		if(form[i] == temp)
		{
			seq++;
		}
		else
		{
			seq=1;
		}
		temp=form[i];
		if(maxSeq < seq)
		{
			maxSeq = seq;
		}
	}
	
	if(maxSeq >= 7)
	{
		cout << "YES";
	}
	else
	{
		cout << "NO";
	}
}
