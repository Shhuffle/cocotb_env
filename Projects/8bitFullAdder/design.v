module adder(
    input  logic [7:0] a, b,
    input  bit cin,
    output logic [7:0] sum,
    output bit carry
);
    assign {carry, sum} = a + b + cin;
endmodule
