#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <chrono>

class Game {
    private:
        unsigned w, h;
        std::vector<std::vector<bool>> grid;

    public:
        Game(std::string filename);

        void save(std::string filename);
        void tick();
};

Game::Game(std::string filename) {
    std::ifstream file(filename);

    unsigned x, y;
    unsigned i = 0;

    while (file >> y >> x) {
        if (i) {
            grid[y + 1][x + 1] = true;
        }
        else {
            w = x + 2;
            h = y + 2;
            grid.resize(h, std::vector<bool>(w));
        }
        i++;
    }
}

void Game::save(std::string filename) {
    std::ofstream out(filename);

    out << w - 2 << " " << h - 2 << "\n";

    for (unsigned y = 1; y < h - 1; y++) {
        for (unsigned x = 1; x < w - 1; x++) {
            if (grid[y][x]) {
                out << y - 1 << " " << x - 1 << "\n";
            }
        }
    }
}

void Game::tick() {
    std::vector<bool> row, row0;

    for (unsigned y = 1; y < h - 1; y++) {
        unsigned y0 = y - 1;
        unsigned y1 = y + 1;
        
        row = std::vector<bool>(w);

        for (int x = 1; x < w - 1; x++) {
            unsigned x0 = x - 1;
            unsigned x1 = x + 1;

            int count = grid[y0][x0] + grid[y0][x] + grid[y0][x1] + grid[y][x0] + grid[y][x1] + grid[y1][x0] + grid[y1][x] + grid[y1][x1];

            if (count == 3) {
                row[x] = true;
            }
            else if (count == 2) {
                row[x] = grid[y][x];
            }
        }

        if (y > 1) {
            grid[y0] = row0;
        }
        row0 = row;
    }

    grid[h - 2] = row;
}

int main() {
    std::cout << "Reading input...\n";
    Game game("input.txt");
    std::cout << "Tick...\n";
    const auto start{std::chrono::steady_clock::now()};
    game.tick();
    const auto end{std::chrono::steady_clock::now()};
    const std::chrono::duration<double> elapsed{end - start};
    std::cout << elapsed.count() << "s\n";
    std::cout << "Writing output...\n";
    game.save("output.txt");
}