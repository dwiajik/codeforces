#include <iostream>

using namespace std;

main()
{
    int n;
    cin >> n;

    int x[4] = {0,0,0,0};

    for (int i = 0; i < n; i++)
    {
        int nChild;
        cin >> nChild;
        switch (nChild)
        {
            case 1:
                x[0]++;
                break;
            case 2:
                x[1]++;
                break;
            case 3:
                x[2]++;
                break;
            case 4:
                x[3]++;
                break;
            default:
                break;
        }
    }

    int temp1 = (x[0] - x[2]) >= 0? x[0] - x[2]: 0;
//    cout << temp1 << endl;
    int temp2 = (2 * x[1] + temp1) % 4 == 0? (2 * x[1] + temp1) / 4: ((2 * x[1] + temp1) / 4) + 1;
//    cout << temp2 << endl;

    cout << x[3] + x[2] + temp2 << endl;
}
