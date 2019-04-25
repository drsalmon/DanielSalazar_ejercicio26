all: euler.dat rk4.dat leapfrog.dat 

%.dat: ejercicio26.x
	./ejercicio26.x

ejercicio26.x: ejercicio26.cpp
	c++ ejercicio26.cpp -o ejercicio26.x
    
ejercicio26.x    

clean:
	rm -rf *.x *.dat