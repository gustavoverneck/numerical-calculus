program teste
    implicit none

    real :: a, b, c
    real :: start, finish

!   Start time cout
    call cpu_time(start)

!   exemplo: bhaskaraSolver(a, b, c)



!   End time count
    call cpu_time(finish)
    print '("Total execution tome: ",f6.3," seconds.")',finish-start

    contains

    function bhaskaraSolver (a, b, c)
c   upgrade futuro -> adicionar opção para enviar output complexo
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

    function gaussJordan (x)
        implicit none
        real, dimension(:) :: x
c       adicionar método gauss-jordan
        print*, 
    end function

end program teste