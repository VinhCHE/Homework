#include <iostream>
using namespace std;
int gal=0; // Number of gallons of gas in the tank
int eff=0; // Fuel efficiency
int price=0; // price per gallons
int costp100 = 0; // cost per hundred miles
int dist = 0; // distance with the gas in the tank
int main()
{
    cout << "Please insert the number of gallons of gas in the tank: ";
    cin >> gal;
    cout << endl << "Please insert the fuel efficiency in miles per gallon: ";
    cin >> eff;
    cout << endl << "Please insert of price per gallon :";
    cin >> price;
    costp100 = 100/eff*price;
    dist = gal * eff;
    cout << "The cost per 100 miles: " << costp100 << endl;
    cout<< " The car can go " << dist <<" miles with the gas on the tank";
}

