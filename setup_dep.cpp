#include <bits/stdc++.h>
using namespace std;

int main()
{
    string ip_network;
    cout << "Enter router's ip:";
    cin >> ip_network;
    cerr << "IP_NETWORK = " << ip_network << endl;

    int device_count;
    cout << "Enter device count= ";
    cin >> device_count;
    cerr << "device_count = " << device_count << endl;

    for (int i=0;i<=device_count-1;i++)
    {
        string a,b;
        cout << "Enter device ip = ";
        cin >> a;
        cerr << "device_ip[" << i << "] = " << a << ":" << endl;
        cout << "Enter device name = ";
        cin >> b;
        cerr << "device_name[" << i << "] = " << b << endl;
    }

    return 0;
}