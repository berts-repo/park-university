# Unit 5: Lecture

Chapter 5: Input/Output

Input/Output consists of two components: mechanical and electronic components. Figure 1 from [1] shows a personal computer consisting of the mechanical components (such as Monitor, keyboard, floppy disk drive and Hard disk drive) and the corresponding electronic components (such as Video controller, keyboard controller, floppy disk controller, and hard disk controller).

Figure 1. Various components of a personal computer system

In an operating system, a device-specific module, called device driver, controls the corresponding I/O hardware. Figure 2 from [1] shows that device drivers are part of the operating system kernel and are usually positioned below the rest of the operating system.

Figure 2. Device drivers are part of the operating system and are usually located below the rest of the operating system.

To accomplish I/O, there are three approaches, namely programmed I/O, interrupt-driven I/O, and DMA.

Programmed I/O

In programmed I/O, the CPU performs the input and output. This is the simplest approach among the three. Take figure 3 from [1] for example. A user process wants to print string “ABCDEFGH”. The user process makes a system call to acquire the printer. If the printer is available, the operating system copies the string from the user space to the kernel space. When the printer’s status register indicates the printer is ready to accept a character, a character is copied to the printer’s data register and gets printed on the page. For each character, the CPU sits in a tight loop and waits for the printer’s status register to become ready for next character. Although this approach is simple, the problem is that the CPU can not do anything else, but sits and waits for the I/O to finish.

Figure 3. The steps in printing a string "ABCDEFGH"

Interrupt-driven I/O

The basic idea is to keep CPU occupied with something else while I/O performs its task, and when I/O finishes its task, it will signal the CPU by sending CPU an interrupt signal. Figure 4 from [1] shows the flow between a device, interrupt controller, and the CPU.

Figure 4. This figure shows how an interrupt works in a personal computer system

Direct Memory Access (DMA)

This is similar to Interrupt-driven I/O approach. Interrupt-driven I/O can be used to transfer a character or a word. DMA is a separate chip managing the transfer of a block of data. When the entire block of data is done transferring, it will send the CPU an interrupt signal. Figure 5 from [1] shows the use of DMA and how a block of data is transferred from a disk controller to main memory.

Figure 5. The steps involved for a DMA transfer

The rest of the chapter then discusses the structure and characteristics of various devices, such as disk, clocks, character-oriented terminals, graphical user interfaces, network terminals, and power management.

This  [link: https://www.youtube.com/watch?v=LNPBr3WvuNg] video provides supplemental information on managing I/O.

Data Transfer Example

Problem: A disk drive rotates at 6500 RPM, and is contains 700 sectors per track.  How much time does it take to read one sector? 

Solution: 6500 RPM is 108.3 revolutions per second (RPS).  Therefore a single revolution takes 9.23 milliseconds (1/108.3 seconds).  To get the time to read one sector we divide 9.23 milliseconds by 700, which gives us 13.19 microseconds.

Supplemental Resource

Chapter 5 Powerpoint Presentation

Chapter 5 Input and Output

References

Modern Operating System. Andrew S. Tanenbaum. Prentice Hall. 4th edition.
