#include "main.h"
#include "testwarpper.h"

TwoDimData storage_buf = {
	{1,1,1,1,1,1,1,1,1},
	// {1,1,1,1,1,1,1,1,1},
	// {1,1,1,1,1,1,1,1,1},
	// {1,1,1,1,2,1,1,1,1},
	// {1,1,1,1,2,1,1,1,1},
	// {1,1,1,1,2,1,1,1,1},
	// {1,1,1,1,1,1,1,1,1},
	// {1,1,1,1,1,1,1,1,1},
	// {1,1,1,1,1,1,1,1,1}
};

int main( void ){

	struct data_* p;
	p = Get_instance();
	data_map_two_dimen_insert(p, 0, storage_buf);
	return 0;
}