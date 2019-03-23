#include <SFML/Graphics.hpp>
#include <iostream>


using namespace std;

int main() {


	sf::Window window(sf::VideoMode(800, 600), "My windows");

	window.setPosition(sf::Vector2i(0, 0)); // position the screen in desktop

	window.setTitle("SFML test"); 

		

	// the program will be running happen an event
	while (window.isOpen()) {

		sf::Event event;
		// check what is the event trigged
		while (window.pollEvent(event)) { //return if event is pending or not
			switch (event.type) {

				case(sf::Event::Closed):
					window.close();
					break;
				case sf::Event::KeyPressed:
					cout << "Key is pressed\n";
					break;
				case sf::Event::KeyReleased:
					cout << "Key was released\n";
					break;
				case sf::Event::MouseWheelScrolled:
					if (event.mouseWheelScroll.wheel == sf::Mouse::VerticalWheel) {
						cout << "wheel type: verticall" << endl;
					}
					else if (event.mouseWheelScroll.wheel == sf::Mouse::HorizontalWheel) {
						cout << "whell type: horizontal" << endl;
					}
					else {
						cout << "whell unknow" << endl;
					}

					std::cout << "wheel movement: " << event.mouseWheelScroll.delta << std::endl;
					std::cout << "mouse x: " << event.mouseWheelScroll.x << std::endl;
					std::cout << "mouse y: " << event.mouseWheelScroll.y << std::endl;
				case sf::Event::MouseButtonPressed:
					if (event.mouseButton.button == sf::Mouse::Left) {
						std::cout << "mouse x: " << event.mouseButton.x << std::endl;
						std::cout << "mouse y: " << event.mouseButton.y << std::endl;
					}
				default:
					break;


			}
			
			if (event.type == sf::Event::Closed)
				window.close();
		}

	}
	
	return 0;
}