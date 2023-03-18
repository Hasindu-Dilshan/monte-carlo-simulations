#include <iostream>
#include <vector>


void show_matrix(std::vector<std::vector<int>> matrix) {
	for(int i = 0; i < matrix.size(); i++) {
		for(int j = 0; j < matrix[i].size(); j++) {
			std::cout << matrix[i][j] << " ";
		}
		std::cout << std::endl;
	}
}

int main() {
	std::vector<std::vector<int>> adjacency_matrix
	{
		{0, 1, 2},
		{1, 0, 3},
		{2, 3, 0}
	};

	show_matrix(adjacency_matrix);

	return 0;
}
