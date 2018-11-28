.. _dci:geolocation:

Geo Location (O)
================

``datacite:geoLocation``

Cardinality
~~~~~~~~~~~

*Optional*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spatial region or named place where the data was gathered or about which the data is focused.

Property geoLocation (O, 0-n)
-----------------------------

Repeat this property to indicate several different locations.

.. _d:geolocationpoint:

Subproperty geoLocationPoint (O)
********************************

A point location in space (occurrences: 0-1).

A point contains a single latitude-longitude pair.

See :ref:`d:geolocation_instructions`.

pointLongitude (M)
++++++++++++++++++

Longitudinal dimension of point (occurrence: 1).

Mandatory if *geoLocationPoint* is used.

pointLatitude (M)
+++++++++++++++++

Latitudinal dimension of point (occurrence: 1).

Mandatory if *geoLocationPoint* is used.

.. _d:geolocationbox:

Subproperty geoLocationBox (O)
******************************

The spatial limits of a place or box (occurrences: 0-1).

**Allowed values, examples, other constraints**

A box is defined by two geographic points. Left lower corner (normally south west), right upper corner (normally north east). Each point is defined by its longitude and latitude.

See :ref:`d:geolocation_instructions`.

westBoundLongitude (M)
++++++++++++++++++++++

Western longitudinal dimension of box. Mandatory if *geoLocationBox* is used.

eastBoundLongitude (M)
++++++++++++++++++++++

Eastern longitudinal dimension of box. Mandatory if *geoLocationBox* is used.

southBoundLatitude (M)
++++++++++++++++++++++

Southern latitudinal dimension of box. Mandatory if *geoLocationBox* is used.

northBoundLatitude (M)
++++++++++++++++++++++

Northern latitudinal dimension of box. Mandatory if *geoLocationBox* is used.

.. _d:geolocationplace:

Subproperty geoLocationPlace (O)
********************************

Description of a geographic location (occurrences: 0-1).

**Allowed values, examples, other constraints**

Free text. Use to describe a geographic location.

Subproperty geoLocationPolygon (O)
**********************************

A drawn polygon area, defined by a set of points and lines connecting the points in a closed chain (occurrences: 0-n).

polygonPoint (M)
++++++++++++++++

A point location in a polygon (occurrences: 4-n). Mandatory if *geoLocationPolygon* is used.

pointLongitude (M)
^^^^^^^^^^^^^^^^^^

Longitudinal dimension of point (occurrence: 1). Mandatory if *polygonPoint* is used.


pointLatitude (M)
^^^^^^^^^^^^^^^^^

Latitudinal dimension of point (occurrence: 1). Mandatory if *polygonPoint* is used.

inPolygonPoint (O)
++++++++++++++++++

For any bound area that is larger than half the earth, define a (random) point inside.

pointLongitude (M)
^^^^^^^^^^^^^^^^^^

Longitudinal dimension of point (occurrence: 1). Mandatory if *inPolygonPoint* is used.

pointLatitude (M)
^^^^^^^^^^^^^^^^^

Latitudinal dimension of point (occurrence: 1). Mandatory if *inPolygonPoint* is used.

.. _d:geolocation_instructions:

Detailed usage instructions
***************************
Use WGS 84 (World Geodetic System) coordinates. Use only decimal numbers for coordinates. Longitudes are -180 to 180 (0 is Greenwich, negative numbers are west, positive numbers are east), Latitudes are -90 to 90 (0 is the equator; negative numbers are south, positive numbers north).

**Remarks**

* adapted from `DataCite MetadataKernel`_ v4.1

Example
~~~~~~~
.. code-block:: xml
   :linenos:

   <datacite:geoLocations>
     <datacite:geoLocation>
       <datacite:geoLocationPlace>Atlantic Ocean</datacite:geoLocationPlace>
       <datacite:geoLocationPoint>
        	<datacite:pointLongitude>31.233</datacite:pointLongitude>
       		<datacite:pointLatitude>-67.302</datacite:pointLatitude>
       </datacite:geoLocationPoint>
       <datacite:geoLocationBox>
       		<datacite:westBoundLongitude>-71.032</datacite:westBoundLongitude>
        	<datacite:eastBoundLongitude>-68.211</datacite:eastBoundLongitude>
       		<datacite:southBoundLongitude>41.090</datacite:southBoundLongitude>
       		<datacite:northBoundLongitude>42.893</datacite:northBoundLongitude>
       </datacite:geoLocationBox>
     </datacite:geoLocation>
   </datacite:geoLocations>

.. _DataCite MetadataKernel: http://schema.datacite.org/meta/kernel-4.1/