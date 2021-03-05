
    A regular strictly convex polygon is a polygon that has the following characteristics:
        all interior angles are less than 180
        all sides have equal length
    For a regular strictly convex polygon with:
        n edges (=n vertices)
        R circumradius
        LaTeX: interiorAngle\:=\:\left(n\:-\:2\right)\cdot\frac{180}{n} i n t e r i o r A n g l e = ( n − 2 ) ⋅ 180 n
        LaTeX: edgeLength,\:s\:=\:2\cdot R\cdot\sin\left(\frac{\pi}{n}\right) e d g e L e n g t h , s = 2 ⋅ R ⋅ sin ⁡ ( π n )
        LaTeX: apothem,\:a\:=\:R\cdot\cos\left(\frac{\pi}{n}\right) a p o t h e m , a = R ⋅ cos ⁡ ( π n )
        LaTeX: area\:=\:\frac{1}{2}\cdot n\cdot s\cdot a a r e a = 1 2 ⋅ n ⋅ s ⋅ a
        LaTeX: perimeter\:=\:n\cdot s p e r i m e t e r = n ⋅ s
    Objective 1 [pts:400]:
        Create a Polygon Class:
            where initializer takes in:
                number of edges/vertices
                circumradius
            that can provide these properties:
                # edges
                # vertices
                interior angle
                edge length
                apothem
                area
                perimeter
            that has these functionalities:
                a proper __repr__ function
                implements equality (==) based on # vertices and circumradius (__eq__)
                implements > based on number of vertices only (__gt__)
        Objective 2 [pts:600]:
            Implement a Custom Polygon sequence type:
                where initializer takes in:
                    number of vertices for largest polygon in the sequence
                    common circumradius for all polygons
                that can provide these properties:
                    max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
                that has these functionalities:
                    functions as a sequence type (__getitem__)
                    supports the len() function (__len__)
                    has a proper representation (__repr__)
            Results:
                Implement these 2 classes as a separate module. Access these modules in a jupyter-notebook (or Google Colab or Deep Note)
                Run Objective 1 module to show that the functionalities are implemented properly
                Run Objective 2 module and show which polygon is efficient for n = 25
                You are submitting link to your GitHub repo, where we can find the 2 modules and your notebook in which you have called and tested them
                All your code must be publicly accessible (make sure to open all links in an incognito window before submitting)

