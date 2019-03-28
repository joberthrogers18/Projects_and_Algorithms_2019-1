#include <SFML/Graphics.hpp>
#include <iostream>


using namespace std;

int main() {

	// create the window
	sf::RenderWindow window(sf::VideoMode(1000, 1000), "My window");
	
	std::vector <sf::RectangleShape> vectorRect(2);

	// define a 120x50 rectangle
	sf::RectangleShape rectangle1(sf::Vector2f(50.f, 50.f));

	rectangle1.setPosition(0.0f, 0.0f);

	// define a 120x50 rectangle
	sf::RectangleShape rectangle2(sf::Vector2f(50.f, 50.f));

	rectangle2.setPosition(50.0f, 0.0f);

	rectangle2.setOutlineThickness(1.f);
	rectangle2.setOutlineColor(sf::Color(0, 0, 0));

	vectorRect[0] = rectangle1;

	vectorRect[0].setFillColor(sf::Color(255,0,0));

	// run the program as long as the window is open
	while (window.isOpen())
	{
		// check all the window's events that were triggered since the last iteration of the loop
		sf::Event event;
		while (window.pollEvent(event))
		{
				switch (event.type) {
					case(sf::Event::Closed):
						window.close();
						break;
					case sf::Event::KeyPressed:
						vectorRect[0].setFillColor(sf::Color(255,255,255));
						break;
					default:
						break;
				}
		}

		// clear the window with black color
		window.clear(sf::Color::Black);
		
		window.draw(vectorRect[0]);

		// end the current frame
		window.display();
	}

	return 0;

}