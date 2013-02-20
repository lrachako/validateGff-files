use strict;

while(my $line = <STDIN>)
{
    if($line =~ m/Parent=([^;]+)/)
    {
        my $parentstr = $1;
        my @values = split(/,/, $parentstr);
        if(scalar(@values) > 1)
        {
            foreach my $parent(@values)
            {
                my $new = $line;
                $new =~ s/Parent=[^;]+/Parent=$parent/;
                print $new;
            }
        }
        else
        {
            print $line;
        }
    }
    else
    {
        print $line;
    }
}
