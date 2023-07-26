module  numerical_recipes
    implicit none

    contains

!   -------------------------------------------------
!   Bhaskara solver
!   Solves a second degree equation of type ax²+bx+c=0
    function bhaskaraSolver(a, b, c)
        implicit none
        real, dimension(2) :: bhaskaraSolver
        real, intent(in) :: a, b, c
        real :: delta, x1, x2

        delta = b**2 - 4*a*c
        if (delta < 0) then
            stop "- Complex root found!"
        else if (a .EQ. 0)then
            stop "- Overflow found!"
        else
            x1 = (0.5/a)*(-b + sqrt(delta))
            x2 = (0.5/a)*(-b - sqrt(delta))
            BhaskaraSolver = (/x1,x2/)
        end if
        return
    end function BhaskaraSolver

!   -------------------------------------------------
!   Gauss-Jordan solver
!   Linearizes Matrix - Solves System of equations
!   FAZER
    function gaussJordan(a)
        implicit none
        
        integer :: i, j, k
        real, dimension(:, :), intent(in) :: a
        real :: n, gaussJordan

        n = size(a)
        gaussJordan = n
        return
    end function gaussJordan

!   -------------------------------------------------
!   FAZER
!   Cubic Spline Interpolation
    function cubicSpline()
        implicit none
        return
    !declarar variaveis
    
    end function cubicSpline

!   -------------------------------------------------
!   FAZER (Numerical Recipes páginas 382~286)
!   Broyden's Method
!   Solves non-linear systems of equations
    function broyden(x)
        implicit none
        return
    end function broyden

!   -------------------------------------------------
!   FAZER
!   Integration
!   ADICIONAR MÉTODO DE INTEGRAÇÃO EM 1 OU MAIS DIMENSÕES
    function integrate(x)
        implicit none
        return
    end function integrate


!   -------------------------------------------------
!   FAZER
!   Fast Fourier Transform
    function fft()
        implicit none
        return
    end function fft




end module solvers