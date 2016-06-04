#include<stdio.h>

main()
{
	int M, N, result;
	scanf("%i %i", &M, &N);
	if(N > M)
	{
		result = M;
		M = N;
		N = result;
		result = 0;
	}
	if(M >= 2)
	{
		result = (M/2)*N;
		if(M % 2 != 0 && N >= 2)
		{
			result += N/2;
		}
	}
    printf("%i", result);
}
