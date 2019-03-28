#include <SFML/Graphics.hpp>
#include <iostream>


using namespace std;

int main() {

	// create the window
	sf::RenderWindow window(sf::VideoMode(1000, 1000), "My window");
	
	std::vector <sf::RectangleShape> vectorRect(1600);


	// run the program as long as the window is open
	while (window.isOpen())
	{
		// check all the window's events that were triggered since the last iteration of the loop
		sf::Event event;
		while (window.pollEvent(event))
		{
			// "close requested" event: we close the window
			if (event.type == sf::Event::Closed)
				window.close();
		}

		// clear the window with black color
		window.clear(sf::Color::Black);

		sf::RectangleShape rect1(sf::Vector2f(30.f, 30.f));

		int auxX = 1;

		for (int i = 0; i < 40; i++) {
			for (int j = 0; j < 40; j++) {
				rect1.setPosition(30 * i, 30 * j);
				rect1.setFillColor(sf::Color(255, 0, 0));
				
				if (i != 0) {
					vectorRect[i*j] = rect1;
					window.draw(vectorRect[i*j]);
				}
				else if(j == 0) {
					vectorRect[i*40+1] = rect1;
					window.draw(vectorRect[i*40+1]);
				}
				else {
					vectorRect[j] = rect1;
					window.draw(vectorRect[j]);
				}
			}

		}

		vectorRect[50].setPosition(0,0);

		
		/*// define a 120x50 rectangle
		sf::RectangleShape rectangle1(sf::Vector2f(50.f, 50.f));

		rectangle1.setPosition(0.0f, 0.0f);

		window.draw(rectangle1);

		// define a 120x50 rectangle
		sf::RectangleShape rectangle2(sf::Vector2f(50.f, 50.f));

		rectangle2.setPosition(50.0f, 0.0f);

		rectangle2.setOutlineThickness(1.f);
		rectangle2.setOutlineColor(sf::Color(0,0,0));


		window.draw(rectangle2);*/

		// end the current frame
		window.display();
	}

	return 0;

}