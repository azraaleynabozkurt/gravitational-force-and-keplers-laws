# Gravitation & Kepler’s Laws: Theory, Simulation, and Visualization

## Overview

This project presents a computational and theoretical study of **gravitational force** and **Kepler’s Three Laws of Planetary Motion**. The goal is to translate fundamental physical principles into clear numerical simulations and graphical representations.

By combining analytical concepts with Python-based visualizations, the project demonstrates how gravitational forces govern planetary motion and orbital dynamics.

## Objectives

- To understand Newton’s Law of Universal Gravitation
- To explore Kepler’s Three Laws at a conceptual and mathematical level
- To simulate planetary orbits using Python
- To visualize orbital motion, areas swept, and period-distance relationships
- To connect theoretical equations with computational results

## Theoretical Background

### Newton’s Law of Universal Gravitation

Every object with mass exerts an attractive force on every other object:

\[
F = G \frac{m_1 m_2}{r^2}
\]

- Force is directly proportional to the product of masses  
- Force is inversely proportional to the square of the distance  

This law explains planetary orbits, moon motion, and the falling of objects.

### Kepler’s First Law – Elliptical Orbits

Each planet moves in an elliptical orbit with the Sun at one focus.  
- A circle is a special case of an ellipse (eccentricity = 0)  
- Real planetary orbits have small eccentricity, slightly deviating from a perfect circle  

### Kepler’s Second Law – Equal Areas

A planet sweeps out equal areas in equal intervals of time:  
- Planet moves faster when closer to the Sun  
- Planet moves slower when farther from the Sun  

This arises from the conservation of angular momentum.

### Kepler’s Third Law – Law of Periods

The square of a planet’s orbital period is proportional to the cube of the semi-major axis of its orbit:

\[
T^2 \propto r^3
\]

- Farther planets take longer to complete an orbit  
- Used to calculate orbital periods of planets, moons, and satellites

## Computational Approach

This project uses **Python**, **NumPy**, and **Matplotlib** to simulate planetary motion and generate visualizations.

**Tools**:  
- NumPy — numerical computation  
- Matplotlib — visualization  

Simulations model:  
- Gravitational forces between celestial bodies  
- Orbital motion along elliptical paths  
- Kepler’s area law and period-distance relationships

## Visualizations and Results

1. **Kepler’s First Law – Elliptical Orbits**  
`results/kepler1.png`  
Demonstrates an elliptical orbit with the Sun at one focus.

2. **Kepler’s Second Law – Equal Areas**  
`results/kepler2.png`  
Shows equal areas swept over equal time intervals along an orbit.

3. **Kepler’s Third Law – Law of Periods**  
`results/kepler3.png`  
Graph showing the relationship between orbital period squared (T²) and semi-major axis cubed (r³).

## Key Insights

- Gravitational force provides centripetal acceleration for orbits  
- Orbital speed varies with distance from the Sun  
- Planetary motion is predictable with Kepler’s laws  
- Computational simulations enhance understanding of theoretical principles

## Applications

- Orbital mechanics for planets, moons, and satellites  
- Astrophysics and space exploration  
- Physics education and computational modeling  
- Understanding orbital dynamics in astronomy

## Articles

This project is supported by detailed written explanations available in both English and Turkish.

* English version: `articles/Gravitational Force and Keplers Laws.eng.pdf`
* Turkish version: `articles/Gravitational Force and Keplers Laws.tr.pdf`

These articles provide a more detailed explanation of circular motion, including theoretical background and real-world examples.

## Project Structure

Gravitation_Kepler_Laws/  
│── README.md  
│── scripts/  
│── results/  
│── articles/  

## Future Improvements

- Multi-body simulations with multiple planets  
- Variable gravitational forces and perturbations  
- Animated simulations of orbital motion  
- Additional visualizations for comparative study

## Author

Azra Aleyna Bozkurt  
Physics Applicant — Computational Physics Focus

## Conclusion

This project demonstrates how gravitational forces and Kepler’s laws govern planetary motion. By combining theoretical equations with Python simulations, it provides a clear and practical understanding of orbital dynamics and celestial mechanics.
