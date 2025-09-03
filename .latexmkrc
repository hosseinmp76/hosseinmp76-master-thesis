add_cus_dep( 'nlo', 'nls', 0, 'makenlo2nls' );
 sub makenlo2nls {
 system( "makeindex -s nomencl.ist -o \"$_[0].nls\" \"$_[0].nlo\"" );
 }
$pdflatex = "xelatex %O %S";
$pdf_mode = 1;
$dvi_mode = 0;
$postscript_mode = 0;
