#include <iostream>

main()
{
	int n, result, temp;
	std::cin >> n;
	int x[4] = {0,0,0,0};
	for(int i = 0; i < n; i++)
	{
		std::cin >> temp;
		if(temp == 4)x[3]++;
		else if(temp == 3)x[2]++;
		else if(temp == 2)x[1]++;
		else if(temp == 1)x[0]++;
	}
	
	result += x[3] + x[2];
	result += x[1]/2;
	
	if(x[2] > x[0])
	{
		if(x[1]%2==1)
		{
			result+=1;
		}
	}
	else
	{
		result += (x[0]-x[2])/4;
		if(x[1]%2==1)
		{
			result+=1;
			if( (x[0]-x[2] - 2) > 0 && (x[0]-x[2] - 2)%4 != 0)
			{
				result +=1;
			}
		}
		else
		{
			if((x[0]-x[2] - 2) > 0 && (x[0]-x[2])%4 != 0)
			{
				result +=1;
			}
		}
	}
	
	std::cout << result;
}
