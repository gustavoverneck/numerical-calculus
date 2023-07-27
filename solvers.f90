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
!   Linearizes Matrix - Solves System of equations
    function diagonalize(x)
        implicit none
        
        integer :: i, j, k, n, p
        real, dimension(:, :), intent(in) :: x
        real, dimension(size(x, 1), size(x, 2)) :: a
        real, dimension(size(x, 1)) :: diagonalize
        real :: m

        n = size(x, 1)  ! n rows
        a = x
         
        ! Zerar triangulo superior
        do j = n, 1, -1
            if (j .GE. 2) then
                do i = j-1, 1, -1
                    m = a(i, j) / a(j, j)
                    do k = 1, n+1, 1
                        a(i, k) = a(i, k) - m*a(j, k)
                    end do
                end do
            end if
        end do

        ! Zerar triângulo inferior
        do j = 1, n, 1  ! para cada linha (elemento da diagonal)
            if (j .LE. n-1) then
                do i = j+1, n, 1
                    m = a(i, j) / a(j, j)
                    do k = 1, n+1 , 1
                        a(i, k) = a(i, k) - m*a(j, k)
                    end do
                end do
            end if
        end do

        ! Adequar diagonal principal
        do j = 1, n, 1
            m = a(j, j)
            do k = 1, n+1, 1
                a(j, k) = a(j, k) / m
            end do
        end do
        diagonalize = a(n + 1, :)
        return
    end function diagonalize

end module numerical_recipes
!   -------------------------------------------------
!   FAZER
!   Cubic Spline Interpolation

!   -------------------------------------------------
!   FAZER (Numerical Recipes páginas 382~286)
!   Broyden's Method
!   Solves non-linear systems of equations

!   -------------------------------------------------
!   FAZER
!   Integration
!   ADICIONAR MÉTODO DE INTEGRAÇÃO EM 1 OU MAIS DIMENSÕES

!   -------------------------------------------------
!   FAZER
!   Fast Fourier Transform
